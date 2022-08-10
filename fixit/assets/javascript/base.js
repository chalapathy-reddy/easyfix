
		function showform() {
			document.getElementById("login").style.display="block";
			document.getElementById("signup").style.display="none";
            document.getElementsByClassName("t")[0].style.height = "350px";

		};
		function showsign() {
			document.getElementById("login").style.display="none";
			document.getElementById("signup").style.display="block";
			document.getElementsByClassName('t')[0].style.height = "465px" ;

		};
		function checkpwd(){
			var p=document.getElementsByClassName("in")[5].value;
			var p2 =document.getElementsByClassName("in")[6].value;
			if(p==p2){
				document.getElementById("message").innerHTML=" ";

			}
			else{
			document.getElementById("message").innerHTML="passwords does not match";

		}
		}