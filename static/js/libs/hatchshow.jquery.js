jQuery.fn.hatchShow = function(){
  $('.hsjs').css('display','inner-block').css('white-space','pre').each(function(){
    var t = $(this);
    t.wrap("<span class='hatchshow_temp' style='display:block'>");
    var pw = t.parent().width();
    while( t.width() < pw ){t.css('font-size', (t.fontSize()+1)+"px"),
      function(){while( t.width() > pw ){t.css('font-size', (t.fontSize()-.1)+"px")}};
    };
  }).css('visibility','visible');
};
jQuery.fn.fontSize = function(){return parseInt($(this).css('font-size').replace('px',''));};
