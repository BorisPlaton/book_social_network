const imageBlock = document.querySelector(".images");

const url = imageBlock.dataset.content;
let nextPage = 2;

const infiniteObserver = new IntersectionObserver(
  ([entry]) => {
    if (entry.isIntersecting && entry.intersectionRatio >= 0.7) {
      loadNewImages()
        .then((response) => {
          imageBlock.insertAdjacentHTML("beforeend", response);
          nextPage++;
          infiniteObserver.unobserve(entry.target);
          infiniteObserver.observe(getLastImageElement());
        })
        .catch((reason) => {
          infiniteObserver.unobserve(entry.target);
          console.error(reason);
        });
    }
  },
  {
    threshold: 0.7,
  }
);

infiniteObserver.observe(getLastImageElement());

function loadNewImages() {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    const urlWithPage = url + `?page=${nextPage}`;
    xhr.open("get", urlWithPage, true);

    xhr.addEventListener("load", () => {
      if (xhr.response) {
        resolve(xhr.response);
      } else {
        reject("Empty page");
      }
    });

    xhr.send();
  });
}

function getLastImageElement() {
  return imageBlock.querySelector("div.col-12:last-child");
}
