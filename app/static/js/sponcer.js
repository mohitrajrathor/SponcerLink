// sponcer.js to handle sponcer dashboard related fucntionality


// balance data
console.log("sponcer.js working!")

// temp function
function tempCall() {
  console.log("temp call")
  return
}

// update campaign
function updateCampaignFunc(id) {
  console.log('updating campaign with id', id)

  const updateForm = document.getElementById(`updateCampaignForm-${id}`)

  let formData = new FormData(updateForm)
  const updateDate = {}

  for (const [key, value] of formData) {
    updateDate[key] = value
  }

  const url = `/api/campaign/updateCampaign/${id}`

  // send request
  fetch(url, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(updateDate)
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


// delete campaign
function deleteCampaign(id) {
  console.log('deleting campaign with id', id)

  const url = `/api/campaign/deleteCampaign/${id}`

  // send request
  fetch(url, {
    method: 'DELETE',
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




// function that tirgger when make-transaction btn got clicked
function addMoney() {
  // get the data
  const balance = document.getElementById('balance')

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


  // update ad request
  function updateAdRequest(id) {
    console.log('updating ad request with id', id)
    
    const updateForm = document.getElementById('updateAdRequestForm-'+id)

    let formData = new FormData(updateForm)
    const updateDate = {}

    for (const [key, value] of formData) {
      updateDate[key] = value
    }

    const url = `/api/request/updateAdRequest/${id}`
  
    // send request
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(updateDate)
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


  // accept proposal request
  function acceptProposal(id) {
    console.log('accepting proposal with id', id)

    const url = `/api/request/acceptProposal/${id}`
    
    // send request
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
  }


  // reject proposal request
  function rejectProposal(id) {
    console.log('rejecting proposal with id', id) 

    const url = `/api/request/rejectProposal/${id}`

    // send request
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
  }



  // campaigns requests

  // create campaigns
  function createCampaign() {
    console.log("creating campaign...")

    // getting form data
    const campForm = document.getElementById('CampaignForm')

    let formData = new FormData(campForm)
    const campData = {}

    for (const [key, value] of formData) {
      campData[key] = value
    }

    console.log(campData)

    const url = `/api/campaign/createCampaign`

    // send request
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(campData)
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
    })
    .catch(error => {
      alert(error)
    })
  
  }

