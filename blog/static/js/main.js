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
        console.log({data});
      $("#myModal .modal-body").html(data.html);
    },
  });
};
var SaveForm =  function(){
  var form = $(this);
  $.ajax({
      url: form.attr('data-url'),
      data: form.serialize(),
      type: form.attr('method'),
      dataType: 'json',
      success: function(data){
          if(data.form_is_valid){
              $('#detail').html(data.html);
              $('#myModal').modal('hide');
          } else {
              $('#myModal .modal-body').html(data.html)
          }
      }
  })
  return false;
}
$(document).ready(function () {
  $(document).on("click", ".show-form", ShowForm);
  $(document).on("submit", ".save-form", SaveForm);
});
