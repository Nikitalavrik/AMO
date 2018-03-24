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
$('#lab5_exec_button').click(function(){
    var row = $('input')
    var matrix = []
    for (i=1;i < row.length-1;i++){
        matrix.push(row[i].value.split(','))
    }
    
    for (k=0;k < matrix.length;k++){
        var p = k
        for (m=0;m < matrix.length;m++){
            if (matrix[m][k] > matrix[p][k]){
                var p = m
            }
        }
        if (p != 0){
            var templ = matrix[k]
            matrix[k] = matrix[p]       
            matrix[p] = templ
        }

        for (j=k+1;j < matrix.length;j++){
            var c = matrix[j][k]/matrix[k][k]

            for (m=k;m < matrix.length+1;m++){
                matrix[j][m] = matrix[j][m] - c*matrix[k][m]

            }
        }
    }
    document.getElementById('answerL5').innerHTML = "Transformation Matrix :"
    var mDiv = document.createElement('div')
    mDiv.id = "matrix"
    mDiv.style.width = (matrix[0].length*77).toString() + "px"

    document.getElementById('answerL5').appendChild(mDiv);
    for (i=0;i < matrix.length;i++){
        for (k=0;k < matrix.length+1;k++){
            mDiv.innerHTML += parseFloat(matrix[i][k]).toFixed(3) + " "
        }
        mDiv.innerHTML += "</br>"
    }

    var x_array = new Array(matrix.length-1);
    var v = matrix[matrix.length-1][matrix.length]/matrix[matrix.length-1][matrix.length-1]
    x_array[matrix.length-1] = v
    
    for (k=matrix.length-1;k > -1;k--){
        var s = 0
        for (j=k+1;j < matrix.length;j++){
            s = s + matrix[k][j]*x_array[j]

        }
        x_array[k] = (matrix[k][matrix.length]- s)/matrix[k][k]
    }

    var iDiv = document.createElement('div')
    iDiv.id = "x_array"
    document.getElementById('answerL5').appendChild(iDiv);
    for (i=0;i < x_array.length;i++){
        iDiv.innerHTML += " X" + (i+1) + " = " + x_array[i] + "</br>"
    }    
})

