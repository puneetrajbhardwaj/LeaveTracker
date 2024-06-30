
$(document).ready(function(){
    $.getJSON("/tracker/getemployeejson",{ajax:true},function(data){
        $('#employee_uid').keyup(function(){
            $('#options').empty();
            for (let index = 0; index < data.length; index++) {
                if(((data[index].employee_name).toLowerCase()).indexOf(($('#employee_uid').val().toLowerCase())) >-1){
                    $('#options').append($('<li>').text(data[index].employee_name+"("+data[index].employee_uid+")").val(data[index].employee_uid));
                }
            
            }


        });

        $('#filter_employee_uid').keyup(function(){
            $('#filter_options').empty();
            for (let index = 0; index < data.length; index++) {
                if(((data[index].employee_name).toLowerCase()).indexOf(($('#filter_employee_uid').val().toLowerCase())) >-1){
                    $('#filter_options').append($('<li>').text(data[index].employee_name+"("+data[index].employee_uid+")").val(data[index].employee_uid));
                }
            
            }


        });
    });
});    

