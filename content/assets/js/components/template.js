window.addEventListener("load", function () {

  (function($) {
    'use strict';
    $(function() {
      var body = $('body');
      var contentWrapper = $('.content-wrapper');
      var scroller = $('.container-scroller');
      var footer = $('.footer');
      var sidebar = $('.sidebar');
      var navbar = $('.navbar').not('.top-navbar');

      function addActiveClass(element) {
        if (current === "") {
          //for root url
          if (element.attr('href').indexOf("base.html") !== -1) {
            element.parents('.nav-item').last().addClass('active');
            if (element.parents('.sub-menu').length) {
              element.closest('.collapse').addClass('show');
              element.addClass('active');
            }
          }
        } else {
          if (element.attr('href').indexOf(current) !== -1) {
            element.parents('.nav-item').last().addClass('active');
            if (element.parents('.sub-menu').length) {
              element.closest('.collapse').addClass('show');
              element.addClass('active');
            }
            if (element.parents('.submenu-item').length) {
              element.addClass('active');
            }
          }
        }
      }

      var current = location.pathname.split("/").slice(-1)[0].replace(/^\/|\/$/g, '');
      $('.nav li a', sidebar).each(function() {
        var $this = $(this);
        addActiveClass($this);
      })

      sidebar.on('show.bs.collapse', '.collapse', function() {
        sidebar.find('.collapse.show').collapse('hide');
      });

      applyStyles();

      function applyStyles() {
      }

      $('[data-toggle="minimize"]').on("click", function() {
        if (body.hasClass('sidebar-toggle-display')) {
          body.toggleClass('sidebar-hidden');
        } else {
          body.toggleClass('sidebar-icon-only');
        }
      });

      $(".form-check label,.form-radio label").append('<i class="input-helper"></i>');

    });
  })(jQuery);

});