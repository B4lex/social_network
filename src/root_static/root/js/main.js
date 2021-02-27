$(function () {
    /* Functions */
    let loadForm = function () {
        let btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-image").modal("show");
            },
            success: function (data) {
                $("#modal-image .modal-content").html(data.html_form);
            }
        });
    };

    let saveForm = function () {

        let form = $(this);
        console.log(form);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            mimeType: "multipart/form-data",
              processData: false,
              contentType: false,
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            success: function (data) {

                if (data.form_is_valid) {
                  console.log('-----');

                  $("#book-table section").html(data.html_image_list);
                  $("#modal-image").modal("hide");
                }
                else {
                  console.log('++++');
                    $("#modal-image .modal-content").html(data.html_form);
                }
            }
        });
        return false

    };


    $(".js-create-image").click(loadForm);
    $("#modal-image").on("submit", ".js-image-create-form", saveForm);
});