$(document).ready( function () {
    // Display opt-in modal after delay
    var hide = Cookies.get('hideOptin');
    if(!hide){
        setTimeout(function() {
            $('#optinModal').modal();
        }, 500);
    }

    $('.modal-header button[type="button"]').bind('click', function ( event ) {
        if (event) event.preventDefault();
        hideOptin(7);
    });

    $("#mc-embedded-subscribe-form").validate({
        submitHandler: function(form) {
            register();
        }
    });
});

function hideOptin(duration) {
    Cookies.set('hideOptin', 'true', { expires: duration });
}

function displayHelp(msg) {
    var helpBlock = $('.modal-body .errors');
    helpBlock.html(msg);
    helpBlock.show();
}

function register() {
    var $form = $('#mc-embedded-subscribe-form');
    $.ajax({
        type: $form.attr('method'),
        url: $form.attr('action'),
        data: $form.serialize(),
        cache       : false,
        dataType    : 'jsonp',
        jsonp       : 'c',
        contentType: "application/json; charset=utf-8",
        error       : function(err) { displayHelp(err); },
        success     : function(data) {
            if (data.result != "success") {
                displayHelp(data.msg);
            } else {
                $('#mc-embedded-subscribe-form').hide();
                $('.modal-body .success').fadeIn();
                setTimeout(function() {
                    $('#optinModal').hide();
                    hideOptin(30);
                }, 10000);
            }
        }
    });
}
