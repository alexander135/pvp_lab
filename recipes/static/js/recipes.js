$(function () {




  $(document).on("click","#js-pagination", function (){
      var num, pageNumber,contid ;
      num = document.getElementById("js-pagination").getAttribute("data");
      pageNumber ="/recipes/content_recipe/" + num+"/";
      contid = "#cont" + num;
      $(contid).load(pageNumber);
      this.remove();
  });

});