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
