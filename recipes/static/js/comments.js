function display_form_errors(errors, $form) {
    for (var k in errors) {
        $form.find('input[name=' + k + ']').after('<div class="error">' + errors[k] + '</div>');
    }
}

$(document).ready(function() {
    var num = "/recipes/commentForm/" + document.getElementById("rec_num").getAttribute("data") + "/";
    $("#new_comment").load(num);
    $("body").on('click',"#add_comment", function(e) {
        e.preventDefault();
        $('#comment_form').ajaxSubmit({
            success: function(data, statusText, xhr, $form) {
                // Удаляем ошибки если были
                $form.find('.error').remove();
                if (data['result'] == 'success') {
                    $("#new_comment:empty").load(num)
                    $("#comment_form:last").remove()
                    $("#nocomment").remove()
                }
                else if (data['result'] == 'error') {
                    // Показываем ошибки
                    display_form_errors(data['response'], $form);
                }
            },
            dataType: 'json',
            url:num,
        });
    });
})