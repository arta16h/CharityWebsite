


function validatePhone(url, csrftoken) {
    let data = { 'phone': document.getElementById('phone').value };
    let isValid = false;
    let message = "";
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        dataType: "json",
        async: false,
        success: function(response) {
            // $('#create-account-form').prepend(`
            //     <div class="alert alert-msg alert-success" role="alert">${response['message']}</div>`
            // );
            // $('.alert-success').fadeOut(3000);
            isValid = true;
            message = response['message'];
        },
        error: function(response) {
            isValid = false;
            message = response.responseJSON['message'];
        }
    });
    return { isValid, message};
}
