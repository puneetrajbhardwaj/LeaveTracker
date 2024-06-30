<script>
$(document).ready(function(){
    $.getJSON("/tracker/getglancejson",{ajax:true},function(data){
        // alert(data)
        for (let index = 0; index < data.length; index++) {
            values=Object.values(data[index])
            // alert(Object.values(data[index]))
            // Assuming you have a table row element and a list of data
            const tableRow = $('<div class="row">');
            $.each(values, function(i, value) {
                // alert(data[index].item)
                const td = $('<div clss="col">').text(value);
                tableRow.append(td);
            });

        $('#glancetable').append(tableRow);

                }
        
    })
}) 
</script>   