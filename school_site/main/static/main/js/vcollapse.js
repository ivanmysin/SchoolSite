function isInt(value) {
  return !isNaN(value) && 
         parseInt(Number(value)) == value && 
         !isNaN(parseInt(value, 10));
}

$.fn.vCollapse = function(s = null) {
  const elm = $(this); // Wrapper element
  const cT = $(this).find('.vcollapse-toggle'); // All .vcollapse-toggle elements
  const cC = $(this).find('.vcollapse-content'); // All .vcollapse-content elements

  let settings = {
    'any': false,
    'onLoad': 0,
    'speed': 300,
    'easing': 'ease-in-out',
  };

  if (s !== null) {
    $.each(s, function( key, value ) {
      settings[key] = value;
    });
  }
  
  function init() {
    // Expand all content on load
    if (settings.onLoad === 'all') {
      cT.addClass('active');
      cC.each(function() {
        const e = $(this);
        e[0].style.height = e[0].scrollHeight + 'px';
      });

      settings.any = true;
    }

    // Collapse all content on load
    if (settings.onLoad === 'none') {
      cT.removeClass('active');
      cC.each(function() {
        const e = $(this);
        e[0].style.height = '0px';
      });
    }

    if (settings.onLoad !== 'all' && settings.onLoad !== 'none') {

      if (!Array.isArray(settings.onLoad)) {
        if (isInt(settings.onLoad)) {
          settings.onLoad = [settings.onLoad];
        } else {
          console.error('Invalid onLoad option: ' + settings.onLoad);
        }
      }

      cC.each(function(index) {
        const e = $(this);
        
        // Collase all content except onLoad
        if (settings.onLoad.includes(index)) {
          e[0].style.height = e[0].scrollHeight + 'px';
          cT.eq(index).addClass('active');
          cC.eq(index).addClass('active');
        } else {
          e[0].style.height = '0px';
        }
      });

      if (settings.onLoad.length > 1) {
        settings.any = true;
      }
    }
    
    // Add transition and overflow styles to all collapse content
    cC.each(function() {
      const e = $(this);

      e[0].style.transition = 'height '+(settings.speed/1000)+'s '+settings.easing;
      e[0].style.overflow = 'hidden';
    });

    cT.each(function(index) {
      const e = $(this);

      e.on('click', function(){
        const target = $($(this).data('target'));
        
        if (settings.any) { // Allowed more than one content to collapse/expand
          if ($(this).hasClass('active')) { // Currently expanded (active)
            $(this).removeClass('active');
            target[0].style.height = '0px';
            target.removeClass('active');
          } else {
            $(this).addClass('active');
            target[0].style.height = target[0].scrollHeight + 'px';
            target.addClass('active');

            if (settings.autoScroll === true) {
              $("html,body").animate(
                {
                  scrollTop: e.offset().top,
                },
                1000
              );
            }
          }
        } else { // Allowed only one content to collapse/expand
          cT.removeClass('active');
          $(this).addClass('active');

          cC.each(function() {
            $(this)[0].style.height = '0px';
            $(this).removeClass('active');
          });

          target[0].style.height = target[0].scrollHeight + 'px';
          target.addClass('active');

          if (settings.autoScroll === true) {
            $("html,body").animate(
              {
                scrollTop: e.offset().top,
              },
              1000
            );
          }
        }

      });
    });
  }

  let vCollapseTimeout;

  $(window).on('resize', function() {
    clearTimeout(vCollapseTimeout);

    vCollapseTimeout = setTimeout(() => {
      $('.vcollapse-content.active').each(function() {
        const elm = $(this);

        elm[0].style.height = 'auto';

        const h = elm[0].scrollHeight;

        elm[0].style.height = h + 'px';
      });
    }, 10);
  });

  init();
}
