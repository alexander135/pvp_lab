$(document).ready(function() {
    $("body").on("click","#like", function (e){
        e.preventDefault()
        var num = this.getAttribute("data");
        var id ="/recipes/like/"+ num  +"/";
        var count = "#like" + num;
        $.ajax({
            url:id,
            method:"get",
            dataType:"html",
            success: function(data){
                $(count)[0].innerHTML = data;
            },
            error:function () {
                alert("error");
            }
        })
    })

});

