

$(document).ready(function(){

     	$("#pre").each(function(){
   		 	var pg_num = $('#pg').text();
       		$("p").text(pg_num);

   		 	 if (pg_num ==0) {
   		 	 	// $("a").removeAttr("href").css("cursor","pointer");
               $("#pre").attr('href', '').css({'border': 'none','width':'0px', 'pointer-events' : 'none'});
               
          	 }
          	 else{
				$("#pre").show();

          	 }
   		 });
   	 	
});
    	
$(document).ready(function(){
     	$("#next").each(function(){
   		 	// alert("next" );
   		 	var pg_num = $('#pg').text();
       		$("p").text(pg_num);

   		 	 if (pg_num == 180) {

              $("#next").attr('href', '').css({'border': 'none','width':'0px', 'pointer-events' : 'none'});

          	 }
          	 else if(pg_num<=180){
				$("#next").show();

          	 }
   		 });
   	 	
});
    	


    