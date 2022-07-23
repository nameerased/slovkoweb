let letters_states = {
    "'": null, 'й': null, 'ц': null, 'у': null, 'к': null, 'е': null, 'н': null, 'г': null, 'ш': null, 'щ': null, 'з': null, 'х': null, 'ї': null,
    'ф': null, 'і': null, 'в': null, 'а': null, 'п': null, 'р': null, 'о': null, 'л': null, 'д': null, 'ж': null, 'є': null,
    '↵': null, 'я': null, 'ч': null, 'с': null, 'м': null, 'и': null, 'т': null, 'ь': null, 'б': null, 'ю': null, '←': null,
};


const wrapper = document.getElementById('keyboard');

const states = ['present', 'absent', 'correct', null];

let index = 0;

wrapper.addEventListener('click', (event) => {
  const isButton = event.target.nodeName === 'BUTTON';
  if (!isButton) {
    return;
  }

  event.target.setAttribute("data-state", states[index]);
  letters_states[event.target.getAttribute("data-key")] = states[index];
  // console.log()
  index = index >= states.length - 1 ? 0 : index + 1;
})


function run_function(param1){
    console.log("running");
    $.ajax({
        url : "q", // the endpoint
        type : "GET", // http method
        data : { param_first : param1,
                // param_second : param2
                }, // data sent with the get request

        // handle a successful response
        success : function(json) {
            console.log("success"); // another sanity check
            console.log(json); // another sanity check

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}
