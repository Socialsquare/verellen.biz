$(document).ready( function () {
    // Display opt-in modal after delay
    var hideOptin = Cookies.get('hideOptin');
    if(!hideOptin){
        setTimeout(function() {
            $('#optinModal').modal();
        }, 500);
    }

    var $form = $('#mc-embedded-subscribe-form');

    if ( $form.length > 0 ) {
        $('form button[type="submit"]').bind('click', function ( event ) {
            if ( event ) event.preventDefault();
            register($form);
        });
    }
    $('.modal-header button[type="button"]').bind('click', function ( event ) {
        if (event) event.preventDefault();
        Cookies.set('hideOptin', 'true', { expires: 7 });
    });
});

function register($form) {
    $.ajax({
        type: $form.attr('method'),
        url: $form.attr('action'),
        data: $form.serialize(),
        cache       : false,
        dataType    : 'json',
        contentType: "application/json; charset=utf-8",
        error       : function(err) { alert("Could not connect to the registration server. Please try again later."); },
        success     : function(data) {
            if (data.result != "success") {
                // Something went wrong, do something to notify the user. maybe alert(data.msg);
                alert(data.msg);
            } else {
                alert(data.msg);
            }
        }
    });
}
