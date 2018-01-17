var temp = $('.circle').data('value');
$('.circle').circleProgress({
    fill: {gradient: ['red', 'orange']},
    startAngle: -Math.PI / 2,
    size: 133
  }).on('circle-animation-progress', function(event, progress) {
    $(this).find('span').html(parseInt(progress*temp));
});