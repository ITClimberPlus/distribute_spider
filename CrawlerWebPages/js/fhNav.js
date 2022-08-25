$(".fhsubnav").hover(
  function () {},
  function () {
    $(".bottomLine").css(
      "width",
      parseFloat($(".selectedsubnav").eq(0).width() + 20) + "px"
    );
    $(".bottomLine").css(
      "left",
      parseFloat($(".selectedsubnav").eq(0)[0].offsetLeft) + "px"
    );
  }
);
$(".subnav li").hover(function () {
  $(".bottomLine").css("width", parseFloat($(this).width() + 20) + "px");
  $(".bottomLine").css("left", parseFloat($(this)[0].offsetLeft) + "px");
});
$(".subnav li").on("click", function () {
  $(".subnav li").removeClass("selectedsubnav");
  $(this).addClass("selectedsubnav");
  $(".bottomLine").css("width", parseFloat($(this).width() + 20) + "px");
  $(".bottomLine").css("left", parseFloat($(this)[0].offsetLeft) + "px");
});
