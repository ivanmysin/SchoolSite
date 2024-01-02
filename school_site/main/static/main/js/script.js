// <![CDATA[
$(function() {

  // Slider
  $('#coin-slider').coinslider({width:960,height:500,opacity:1});

  // Radius Box
  $('.menu_nav ul, .menu_nav ul li a, .content .mainbar h2, .content .sidebar h2, .content .mainbar .article, .content .sidebar .gadget, .post_content a.rm, .content p.pages span, .content p.pages a').css({"border-radius":"6px", "-moz-border-radius":"6px", "-webkit-border-radius":"6px"});
  //$('.post_content a.rm, .content p.pages span, .content p.pages a').css({"border-radius":"6px", "-moz-border-radius":"6px", "-webkit-border-radius":"6px"});
  //$('.article a.com').css({"border-top-right-radius":"10px", "border-bottom-right-radius":"10px", "-moz-border-radius-topright":"10px", "-moz-border-radius-bottomright":"10px", "-webkit-border-top-right-radius":"10px", "-webkit-border-bottom-right-radius":"10px"});
  //$('.content p.pages span, .content p.pages a').css({"border-radius":"16px", "-moz-border-radius":"16px", "-webkit-border-radius":"16px"});
  //$('.menu_nav ul').css({"border-top-left-radius":"10px", "border-bottom-left-radius":"10px", "-moz-border-radius-topleft":"10px", "-moz-border-radius-bottomleft":"10px", "-webkit-border-top-left-radius":"10px", "-webkit-border-bottom-left-radius":"10px"});
  //$('p.infopost, .content .sidebar h2').css({"border-top-left-radius":"6px", "border-bottom-left-radius":"6px", "-moz-border-radius-topleft":"6px", "-moz-border-radius-bottomleft":"6px", "-webkit-border-top-left-radius":"6px", "-webkit-border-bottom-left-radius":"6px"});
  //$('.searchform, .content .sidebar .gadget, .content .mainbar .article, .content p.pages').css({"border-top-left-radius":"10px", "border-top-right-radius":"10px", "-moz-border-radius-topleft":"10px", "-moz-border-radius-topright":"10px", "-webkit-border-top-left-radius":"10px", "-webkit-border-top-right-radius":"10px"});

});	

// Cufon
Cufon.replace('h1, h2, h3, h4, h5, h6, .post_content a.rm, .menu_nav ul li a', { hover: true });
//Cufon.replace('h1', { color: '-linear-gradient(#fff, #ffaf02)'});
//Cufon.replace('h1 small', { color: '#8a98a5'});

// ]]>