var ShowForm = function () {
  var btn = $(this);
  $.ajax({
    url: btn.attr("data-url"),
    type: "get",
    dataType: "json",
    beforeSend: function () {
      $("#myModal").modal("show");
    },
    success: function (data) {
      $("#myModal .modal-body").html(data.html);
    },
  });
};
var PostForm = function (form, callback) {
  $.ajax({
    url: form.attr("data-url"),
    data: form.serialize(),
    type: form.attr("method"),
    dataType: "json",
    success: callback
  });
  return false;
};
var SaveForm = function (evt) {
  evt.preventDefault();
  var form = $(this);
  PostForm(form, function (data) {
    if (data.form_is_valid) {
      $("#detail").html(data.html);
      $("#myModal").modal("hide");
    } else {
      $("#myModal .modal-body").html(data.html);
    }
  });
};
var DeleteForm = function (evt) {
  evt.preventDefault();
  var form = $(this);
  var postId = "#post" + form.attr("data-id");
  PostForm(form, function (data) {
    if (data.form_is_valid) {
      $(postId).remove();
      $("#myModal").modal("hide");
    } else {
      $("#myModal").modal("hide");
    }
  });
};
$(document).ready(function () {
  $(document).on("click", ".show-form", ShowForm);
  $(document).on("submit", ".save-form", SaveForm);
  $(document).on("submit", ".delete-form", DeleteForm);
});
