



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

function verifyOTP(url, otp_code, csrftoken) {
    let data = { 'otp_code': otp_code };
    let isValid = false;
    let message = "";
    let fullUrl = url + "?" + "otp_request=verify_otp";
    alert("fullUrl: " + fullUrl)
    $.ajax({
        type: "POST",
        url: fullUrl,
        data: data,
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        dataType: "json",
        async: false,
        success: function(response) {
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

// CSRF token for Django

// Function to handle the AJAX request

function sendOTP(url, csrftoken) {
    let data = {
        'otp_identifier': document.getElementById('phone').value,
        'otp_type': 'sms'
    };

    return new Promise((resolve, reject) => {
        $.ajax({
            type: "POST",
            url: url,
            data: data,
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            dataType: "json",
            success: function(response) {
                resolve({ message: response.message });
            },
            error: function(response) {
                reject({ message: response.responseJSON.message });
            }
        });
    });
}




