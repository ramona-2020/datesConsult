

function clearContacts() {
    const users = document.querySelector('#users tbody');
    while (users.hasChildNodes()) {
        users.removeChild(users.firstChild);
    }
}

function getContacts(url){
    clearContacts();

      fetch(url, {
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        }
      })
      .then(response => response.json())
      .then(data => {
          const users = document.querySelector('#users tbody');
          data.context.forEach(user => {
              const tr = document.createElement('tr');

              const tdCheck = document.createElement('td');
              const tdCheckbox = document.createElement('input');
              tdCheckbox.type = 'checkbox';

              tdCheck.appendChild(tdCheckbox);

              const tdName = document.createElement('td');
              tdName.textContent = user.name;

              const tdEmail = document.createElement('td');
              tdEmail.textContent = user.email;

              tr.appendChild(tdCheck);
              tr.appendChild(tdName);
              tr.appendChild(tdEmail);

              users.appendChild(tr);
          })
      });
}

function getSelectedEmails(e) {
    e.preventDefault();

    let checkboxes = Array.from(document.querySelectorAll('input[type=checkbox]'));
    let selectedEmails = [];

    checkboxes.filter((item) => {
        return item.checked;
    }).map((item) => {
        const email = item.closest('tr').querySelector('td:last-child');
        selectedEmails.push(email.textContent);
    })


    $.ajax({
        type: 'GET',
        url:  '',
        dataType: 'json',
        contentType: 'json',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
        },
        data: {
            'list': selectedEmails.join('&'),
        },
        success: () => {
            console.log('Emails have been sent successfully');
            $('#alert-success').show();
            setTimeout(() => {
                $('#alert-success').hide();
            }, 5000);
        },
        error: (error) => {
            console.log('Error sending emails');
        }
    })
}

function createContact(url, data) {
    fetch(url, {
        method: 'POST',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookieByName('csrftoken'),
        },
        body: JSON.stringify({data: data})
    }).then((response) => response.json());
}


function selectEmails() {
    const submit = document.getElementById('submit');
    submit.addEventListener('click', getSelectedEmails);
}


function getCookieByName(name='csrftoken') {
    let cookieValue = null;
    let cookies = document.cookie;
    if (cookies) {
        // csrftoken=gsanU0EwxGV3bXYctEgDxjuP45fNObxo
        cookies = cookies.split('&');
        for (const cookie of cookies) {
            if (cookie.trim().substr(0, name.length) === name) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
        }
    }

    return cookieValue;
}

window.onload = () => {
    getCookieByName('csrftoken');
}