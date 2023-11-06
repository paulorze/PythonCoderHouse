let forms = document.querySelectorAll('.card__form');
forms.forEach(form => {
    form.addEventListener('submit', handleSubmit);
});

function handleSubmit(event) {
    console.log('hola')
    event.preventDefault();
    let form = event.target;

    fetch(form.action, {
        method: form.method,
        body: new FormData(form),
        headers: {
            "X-CSRFToken": form.querySelector('input[name="csrfmiddlewaretoken"]').value,
        },
    })
        .then(response => response.json())
        .then(data => {
            displayToast(data.message, data.success);
        })
        .catch(error => {
            console.error(error);
        });
};

function displayToast(message, isSuccess) {
    Toastify({
        className: 'toasty',
        text: message,
        duration: 2000,
        gravity: "top",
        position: "right",
        style: {
            background: isSuccess ? "#4CAF50" : "#F44336",
            fontsize: "1.25rem"
        }
    }).showToast();
};