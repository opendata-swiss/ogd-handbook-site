$(document).ready(function() {
    $('table').addClass('table table-striped table-hover');

    // Language switcher
    var lang = $('html').attr('lang');
    var $curlang = $('#lang-switch li[lang="' + lang + '"]').addClass('active');
    $('#lang-button .name').html($curlang.text());

    // Stylise internal resource links
    $('.page .entry-content a[href^="/"]').each(function() {
      var href = $(this).attr('href');
      if (href.indexOf('/library/') >= 0) {
        $(this).addClass('library-ref')
          .prepend('<i class="fa fa-file-text-o"></i>&nbsp;');
      } else if (href.indexOf('/tag/') >= 0) {
        $(this).addClass('tags-ref')
          .prepend('<i class="fa fa-tag"></i>&nbsp;');
      } else if (href.indexOf('/pages/') < 0) {
        $(this).addClass('article-ref')
          .prepend('<i class="fa fa-bookmark-o"></i>&nbsp;');
      }
    });

    // Fancy checklists
    $('checkbox')
      .prepend('<i class="fa fa-circle-o"></i>')
      .click(function() {
        $(this).toggleClass('active')
          .find('.fa:first')
            .toggleClass('fa-circle-o')
            .toggleClass('fa-check-circle-o');
      });

    // Wrap tag links as buttons
    $('tags a').addClass('btn btn-sm');

    // Simple thumbnails
    $('article .entry-content > p > img').click(function() {
      var clearPopups = function(me) {
        $('article .entry-content > p > img.zoomed-in').each(function() {
          if (me === null || $(this)[0] !== me[0]) $(this).removeClass('zoomed-in');
        });
      };
      clearPopups($(this).toggleClass('zoomed-in'));
    });

    // Enable commenting function using Hypothes.is
    $('#annotate-start').click(function() {
      if ($('#annotate-popup').hasClass('disabled')) { return; }
      $('#annotate-popup')
        .addClass('disabled')
        .find('i')
          .removeClass('fa-comment-o').addClass('fa-check');
      $('body')
        .append('<script async defer src="https://hypothes.is/embed.js"></script>');
    });
});

function validateForm(query) {
  return (query.length > 0);
}
