const imageBlock = document.querySelector(".images");

window.addEventListener("scroll", () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
    pagination.loadImages();
  }
});

const pagination = {
  next_page: 2,
  url: imageBlock.dataset.content,
  loadImages: () => {
    pagination
      .loadNewImages()
      .then((response) => {
        imageBlock.insertAdjacentHTML("beforeend", response);
        next_page++;
      })
      .catch((error) => console.error(error));
  },
  loadNewImages: () => {
    return new Promise((resolve, reject) => {
      const xhr = new XMLHttpRequest();
      const url_with_page = pagination.url + `?page=${pagination.next_page}`;
      xhr.open("get", url_with_page, true);
      xhr.addEventListener("load", () => {
        resolve(xhr.response);
      });
      xhr.send();
    });
  },
};
