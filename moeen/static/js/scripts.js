 // add spinner when button is pressed
 




// If text is arabic activate the button
function checkInputText(inputText) {
    let isArabic = /[\u0600-\u06FF]/;

    if (isArabic.test(inputText.value)) {
      var processBtn = document.getElementById("process-btn");
      if (inputText.value.trim() != "") {
        processBtn.disabled = false;

      } else {
        processBtn.disabled = true;

      }
    }
  };



// If button is pressed

function processText() {

  console.log("This is process text");
  var spinner = document.getElementById("spinner");
  spinner.style.display = "inline-block";

  var processBtn = document.getElementById("process-btn");
  processBtn.disabled  = true;

  };


    // processing effect on button

    //mainBtn.style.display='none';

    // document.getElementById('loadingGif').style.display = "block";
    // setTimeout(function() {
    //   document.getElementById('loadingGif').style.display = "none";
    // },2000);


    // show widget with fade 

		// var mainForm = document.getElementById("main-form");
		// var processedTextDiv = document.getElementById("processed-text-div");
		// var processBtn = document.getElementById("process-btn");

		// if (mainForm.style.display === "block"){

		// 	mainForm.style.display = "none";
		// 	processedTextDiv.style.display = "block";

		// 	processBtn.innerHTML = 'عودة';



		// }else {
       
    //    // hide form and show processed paragraph

		// 	mainForm.style.display = "block";
		// 	processedTextDiv.style.display = "none";

		// 	processBtn.innerHTML = 'تحليل';

		// }
		




  // When a word is clicked open its meaning 


/* function openTextMeaning(spanWord) {
    var mainAcc = document.getElementById("words-info-accordion").children;
    var i;

    for (i = 0; i < mainAcc.length; i++){

    	btnAcc = document.getElementById("accordion-btn-" + (i+2));
    	//console.log(btnAcc)
    	console.log(spanWord.innerText)

    	if (btnAcc.textContent == spanWord.innerText) {
    		btnAcc.click();
    	}

    } */





