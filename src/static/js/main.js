;(function () {
    const modal = new bootstrap.Modal(document.getElementById("modal"))
  
    htmx.on("htmx:afterSwap", (e) => {
      if (e.detail.target.id == "notesModal") {
        modal.show()
      }
    })
  
    htmx.on("htmx:beforeSwap", (e) => {
      if (e.detail.target.id == "notesModal" && !e.detail.xhr.response) {
        modal.hide()
        e.detail.shouldSwap = false
      }
    })

    htmx.on("hidden.bs.modal", () => {
        document.getElementById("notesModal").innerHTML = ""
    })
})()

;(function() {
  const toastE1 = document.getElementById('toast')
  const toastBody = document.getElementById('toast-body')
  const toast = new bootstrap.Toast(toastE1, { delay: 2000 })

  htmx.on("showMessage", (e) => {
      toastBody.innerText = e.detail.value
      toast.show()
  })
})()
