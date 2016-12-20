from partner.models import Partner
from django.utils import timezone
import os
import StringIO
import hashlib
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import zipfile, tempfile, os

def user_is_expired(user):
    partner = get_partner(user)
    if partner and partner.expiryDate:
        if partner.expiryDate < timezone.now():
            return True
    return False

def get_partner(user):
    p = Partner.objects.filter(user__id=user.id)

    if p.exists():
        return p.first()

    return None

try:
    from boto.s3.connection import S3Connection
    from boto.s3.key import Key
except ImportError:
    raise ImproperlyConfigured, "Could not load Boto's S3 bindings."


FILE_ROOT = 'media'
LOCAL_DIRECTORY = '../media/'
US_DIRECTORY = 'us'
EU_DIRECTORY = 'eu'

def syncS3(version = US_DIRECTORY):
    connection = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    bucket = connection.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
    s3_keys = bucket.list()

    directory = 'media/media\\product_tear_sheets'
    if (version == EU_DIRECTORY):
        directory = 'media/media\\product_tear_sheets_metric'

    save_keys(s3_keys, directory, version)

def save_keys(keys, directory, version):
    for key in keys:
        key_string = str(key.key)
        parent_folder = "\\".join(key_string.split("/")[0:2])
        parent_folder = os.path.join(FILE_ROOT, parent_folder)
        if directory == parent_folder:
            key_path = os.path.join(parent_folder, key_string.split("/")[-1])
            local_dir_path = os.path.join(LOCAL_DIRECTORY, version)
            local_path = os.path.join(LOCAL_DIRECTORY, version, key_path.split('/')[-1])
            if not os.path.exists(local_dir_path):
                os.makedirs(local_dir_path)
            if not os.path.exists(local_path):
                save_to = open(local_path, "wb")
                key.get_file(save_to)
                save_to.close()
                # print "saved: %s" % local_path
            else:
                # etag holds the md5 for the key, wrapped in quotes
                s3_md5 = key.etag.strip('"')
                local_md5 = hashlib.md5(open(local_path, "rb").read()).hexdigest()
                # if s3_md5 == local_md5:
                    # print "already exists, file the same: %s" % local_path
                # else:
                if not s3_md5 == local_md5:
                    save_to = open(local_path, "wb")
                    key.get_file(save_to)
                    save_to.close()
                    # print "file changed, overwrote: %s" % local_path

def generateZipResponse(version):
    temp = tempfile.TemporaryFile()
    zf = zipfile.ZipFile(temp,
        mode='w',
        compression=zipfile.ZIP_DEFLATED,
    )
    try:
        local_dir_path = os.path.join(LOCAL_DIRECTORY, version)
        for f in os.listdir(local_dir_path):
            if f.endswith(".pdf"):
                pdf = open(local_dir_path + '/' + f, 'r')
                zf.writestr(f, pdf.read())
                pdf.close()
    finally:
        zf.close()
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    v = version
    if version == EU_DIRECTORY:
        v = 'metric'

    response['Content-Disposition'] = 'attachment; filename=Tear_sheets_' + v + '.zip'
    response['Content-Length'] = temp.tell()
    temp.seek(0)
    return response


def generateZipCategoriesResponse(version, products, category_slug):
    temp = tempfile.TemporaryFile()
    zf = zipfile.ZipFile(temp,
        mode='w',
        compression=zipfile.ZIP_DEFLATED,
    )
    try:
        for product in products:
            if version == US_DIRECTORY and product.tearsheet:
                f = product.tearsheet.url.split('/')[-1]
            elif product.tearsheet_metric:
                f = product.tearsheet_metric.url.split('/')[-1]
            else:
                continue

            local_path = os.path.join(LOCAL_DIRECTORY, version, f)
            if os.path.exists(local_path):
                pdf = open(local_path, 'r')
                zf.writestr(f, pdf.read())
                pdf.close()
    finally:
        zf.close()
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    v = version
    if version == EU_DIRECTORY:
        v = 'metric'

    response['Content-Disposition'] = 'attachment; filename=' + category_slug + '_tear_sheets_' + v + '.zip'
    response['Content-Length'] = temp.tell()
    temp.seek(0)
    return response
