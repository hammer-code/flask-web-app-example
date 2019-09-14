const editButtons = document.querySelectorAll('.edit-button')

for (var i = 0; i < editButtons.length; i++) {
  var button = editButtons[i];

  button.addEventListener('click', function (event) {
    var bookId = event.target.dataset.id;
    var editForm = document.querySelector('#book-edit-form-' + bookId);
    var bookInfo = document.querySelector('#book-info-' + bookId);

    editForm.classList.toggle('hidden');
    bookInfo.classList.toggle('hidden');
  });
}
