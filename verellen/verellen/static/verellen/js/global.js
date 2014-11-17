var positionFooter = function() {
    var footerHeight = $('.footer').outerHeight();
    $('body').css('margin-bottom', footerHeight + 'px');
};

$(window).resize(function() {
    positionFooter();
});

$(positionFooter);
