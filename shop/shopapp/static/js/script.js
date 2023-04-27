// $(document).ready(function () {
//   $(".send_btn").click(function (e) {
//     e.preventDefault()
//     $.ajax({
//       url: $(".url").val(),
//       type: "GET",
//       data: {id:$(this).val()},
//       success: function () {
//       },
//     });
//   });
// });

$(document).ready(function () {
  $(".send_btn").click(function (e) {
    e.preventDefault();
    const csrf = $("#form").find("input[name=csrfmiddlewaretoken]"); // first variant
    // const csrf = $('#form input[name="csrfmiddlewaretoken"]'); // second variant
    $.ajax({
      url: $(".url").val(),
      type: "POST",
      data: { csrfmiddlewaretoken: csrf.val(), id: $(this).val()},
      success: function () {},
    });
  });
});

$(document).ready(function () {
  $(".delete_btn").click(function (e) {
    e.preventDefault();
    let idForm = $(`#${$(this).val()}`);
    const csrf = idForm.find("input[name=csrfmiddlewaretoken]"); // first variant
    // const csrf = $('#form input[name="csrfmiddlewaretoken"]'); // second variant
    $.ajax({
      url: $(".url").val(),
      type: "POST",
      data: { csrfmiddlewaretoken: csrf.val(), id: $(this).val() },
      success: function () {
        idForm.remove();
        let del_div = document.querySelector(".basket_div");
        console.log(del_div);
      },
    });
  });
});
