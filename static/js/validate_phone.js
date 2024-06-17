



function validatePhone(url, phone, validate_for, csrftoken) {
    let data = { 'phone': phone, 'validate_for': validate_for };
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


function verifyOTP(url, otp_code, otp_request, csrftoken) {
    let data = { 'otp_code': otp_code };
    let isValid = false;
    let message = "";
    let fullUrl = url + "?" + "otp_request=" + otp_request;
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

function sendOTP(url, otp_identifier, otp_type, csrftoken) {
    let data = {
        'otp_identifier': otp_identifier,
        'otp_type': otp_type
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




