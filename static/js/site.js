console.log(1)
$('#lab1_part1').submit(function(e){
    $.post('/lab1_part1/', $(this).serialize(), function(data){
        $('#answerL1P1').html("Answer : " + data.toString())
    });
    e.preventDefault();
  });

$('#lab1_part2').submit(function(e){
$.post('/lab1_part2/', $(this).serialize(), function(data){
    $('#answerL1P2').html("Answer : " + data.toString())
});
e.preventDefault();
});

$('#lab1_part3').submit(function(e){
    $.post('/lab1_part3/', $(this).serialize(), function(data){
        $('#answerL1P3').html("Answer : " + data.toString())
    });
    e.preventDefault();
});


