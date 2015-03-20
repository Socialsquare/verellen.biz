var positionFooter = function() {
    var footerHeight = $('.footer').outerHeight();
    $('body').css('margin-bottom', footerHeight + 'px');
};

$(window).resize(function() {
    positionFooter();
});

$(positionFooter);

$(function() {
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });
    $("#sidebar-wrapper .close").click(function(e) {
        e.preventDefault();
        $("#wrapper").removeClass("toggled");
    });
});