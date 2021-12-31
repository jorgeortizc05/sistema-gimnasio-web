function message_error(obj) {
    if (typeof (obj) === 'object') {
        var html = '<ul style="text-align: left">';
        $.each(obj, (key, value) => {
            html += '<li>' + key + ': ' + value + '</li>';
            // console.log("Key: " + key);
            // console.log("Value: " + value);
        });
        html += '</ul>'
    }else{
        html = '<p>'+obj+'</p>';
    }
    Swal.fire({
        title: "Error",
        html: html,
        icon: 'error'
    })


}