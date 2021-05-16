var since = 0;

$(document).ready(function() {
    setInterval(function(){
        $ajax({
            type:"GET",
            url:"/recipes/get_recipe/",
            data:{since:since},
        }).success(function(recipe){
            if(!recipe){
                return
            }
            $("#newrec")[0].innerText = recipe.title
            since = recipe.created_at
        })
    },5000)



})
