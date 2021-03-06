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


  let CloseModal = function () {
      $("#modal-image").modal("hide");
  };

  let openDetail = function () {
      let btn = $(this);
      console.log(btn);
      $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-image").modal("show");
      },
      success: function (data) {
        $("#modal-image .modal-content").html(data.html_detail);
      }
    });
  };


  let likeImage = function () {
      let idObject = $(this).data('id');
      let action_data = $(this).attr('data-action');

      $.ajax({
          type: 'POST',
          url: "/images/like/",
          data: {
              id: $(this).attr('data-id'),
              action: $(this).attr('data-action')
          },
          success: function (data) {
            let conteiner = $('#'+ idObject);
            console.log(conteiner.html());
            if (data['status'] === 'ok') {
                let img_hart = conteiner.children("a.like-button").children("svg");
                let previous_likes = parseInt(conteiner.children("span.count").text());

                if (action_data==='like'){
                    conteiner.children("a.like-button").attr('data-action', "unlike");
                    img_hart.addClass("add-like-image");
                    conteiner.children("span.count").text(previous_likes+1)
                }
                else if (action_data==='unlike'){
                    conteiner.children("a.like-button").attr('data-action', "like");
                    img_hart.removeClass("add-like-image");
                    conteiner.children("span.count").text(previous_likes-1)
                }
            }

          }
      });
      return false;

  };
  //   let likeImage = function () {
  //     let idObject = $(this).data('id');
  //     let action_data = $(this).attr('data-action');
  //
  //     $.ajax({
  //         type: 'POST',
  //         url: "/images/like/",
  //         data: {
  //             id: $(this).attr('data-id'),
  //             action: $(this).attr('data-action')
  //         },
  //         success: function (data) {
  //           let conteiner = $('#'+ idObject);
  //           console.log(conteiner.html());
  //           if (data['status'] === 'ok') {
  //               let img_hart = conteiner.children("a.like-button").children("svg");
  //               let previous_likes = parseInt(conteiner.children("span.count").text());
  //
  //               if (action_data==='like'){
  //                   conteiner.children("a.like-button").attr('data-action', "unlike");
  //                   img_hart.addClass("add-like-image");
  //                   conteiner.children("span.count").text(previous_likes+1)
  //               }
  //               else if (action_data==='unlike'){
  //                   conteiner.children("a.like-button").attr('data-action', "like");
  //                   img_hart.removeClass("add-like-image");
  //                   conteiner.children("span.count").text(previous_likes-1)
  //               }
  //           }
  //
  //         }
  //     });
  //     return false;
  //
  // };


  let saveForm = function () {
    let form = $(this);
    $.ajax({
        url: form.attr("action"),
        type: form.attr("method"),
        dataType: 'json',
        data: new FormData(this),
        processData: false,
        contentType: false,
        success: function (data) {
        if (data.form_is_valid) {
          $("main section").html(data.html_image_list);
          $("#modal-image").modal("hide");
        }
        else {
          $("#modal-image .modal-content").html(data.html_form);
        }
      }
    });
    return false;

  };
  let csrftoken = Cookies.get('csrftoken');
  function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
      }
    });


    $(document).on("click", ".js-create-image", loadForm);
    $(document).on("submit", ".js-image-create-form", saveForm);

    $(document).on("click", ".js-update-image", loadForm);
    $(document).on("submit", ".js-image-update-form", saveForm);


    $(document).on("click", ".js-delete-image", loadForm);
    $(document).on("submit", ".js-image-delete-form", saveForm);

    $(document).on("click", ".close", CloseModal);

    $(document).on("click", ".js-detail-image", openDetail);


    $(document).on("click", ".like-button", likeImage);

});

