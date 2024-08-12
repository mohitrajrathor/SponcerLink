// sponcer.js to handle sponcer dashboard related fucntionality

// fetch data from page
const dataDiv = document.getElementById('data')
const id = dataDiv.getAttribute('data-id')                  // user id
const username = dataDiv.getAttribute('data-username')      // username
const usertype = dataDiv.getAttribute('data-usertype')      // usertype
// balance data
const balance = document.getElementById('balance')

console.log("sponcer.js working!")



// function that tirgger when make-transaction btn got clicked
function addMoney() {
  // get the data
  const amount = document.getElementById('amt').value
  const upiId = document.getElementById('upi-id').value
  console.log(amount, upiId)

  if (!(amount && upiId)) {
    alert('Please enter amount and UPI Id')
    return
  }

  if (amount < 100) {
    alert('Amount should be greater than 100')
    return
  }

  // update div with message
  const messageDiv = document.getElementById('money-message')
  messageDiv.innerHTML = '<div class="alert alert-light" role="alert">Transaction in progress...</div>'

  // send request
  const url = `/api/transaction/credit?id=${id}&amount=${amount}&upiId=${upiId}`
  
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(response => response.json())
    .then(data => {
      balance.innerHTML = data['updt_amt']
      alert('Transaction Successful')
      messageDiv.innerHTML = '<div class="alert alert-success" role="alert">Transaction Successful</div>'
      document.getElementById('amt').value = ''
      document.getElementById('upi-id').value = ''
    })
    .catch(error => {
      messageDiv.innerHTML = '<div class="alert alert-danger" role="alert">Error in transaction</div>'
      alert('Error in transaction')
    })

  return

}

// add money to sponcer 
const makeTransaction = document.getElementById('make-transaction')
if (makeTransaction) {
  makeTransaction.addEventListener('click', addMoney)
}


// delete ad request
function cancelAdRequest(id) {

  console.log('deleting ad request with id', id)
  const url = `/api/request/cancelAdRequest/${id}`

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
    console.log(response)
    if (response.ok) {
      return response.json()
    }
  })
    .then(data => {
      alert(data['message'])
      location.reload()
      return 
    }).catch(error => {
      alert(error)
    })

    return

  }
