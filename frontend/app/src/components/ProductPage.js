import { useEffect, useState, useRef } from "react";
import axios from "./Axios";
import Naavbar2 from "./Naavbar2";
import "./PP.css";
import ArrowForwardIosIcon from "@mui/icons-material/ArrowForwardIos";
import ArrowBackIosNewIcon from "@mui/icons-material/ArrowBackIosNew";

const ProductPage = () => {
  const [data, setData] = useState([]);
  const [render, setRender] = useState(false);

  const thumbImagesRef = useRef([]);
  const activeImageRef = useRef(null);
  const overlayRef = useRef(null);
  const nextBtnRef = useRef(null);
  const prevBtnRef = useRef(null);
  const lightBoxWrapperRef = useRef(null);
  const lightBoxContentRef = useRef(null);
  const currentIndexRef = useRef(0);

  const getData = async () => {
    try {
      const res = await axios.get("fetchall/", {
        headers: { "Content-Type": "application/json" },
      });
      setData(res.data.data);
      console.log(res.data.data);
      if (res.data.data[0]?.title !== null) setRender(true);
      console.log(res);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    getData();
  }, []);

  useEffect(() => {
    const thumbImagesDivs = Array.from(
      document.querySelectorAll(".product-images-wrapper .thumb-image")
    );
    thumbImagesRef.current = thumbImagesDivs;
    activeImageRef.current = document.querySelector(
      ".product-images-wrapper .preview-image"
    );
    overlayRef.current = document.querySelector(".overlay");
    nextBtnRef.current = document.querySelector(
      ".preview-image-wrapper .arrows .next"
    );
    prevBtnRef.current = document.querySelector(
      ".preview-image-wrapper .arrows .prev"
    );
    lightBoxWrapperRef.current = document.querySelector(".lightbox-wrapper");
    lightBoxContentRef.current = document.querySelector(".lightbox-content");

    function handleThumbsSrc() {
      thumbImagesDivs.forEach((thumb) => {
        let thumbImage = thumb.querySelector("img");
        let setOriginalSrc = thumbImage
          .getAttribute("src")
          .replace("-thumbnail", "");
        thumb.dataset.original = setOriginalSrc;
      });
    }
    handleThumbsSrc();

    function showThumbsAsActive(thumbnails, previewActive) {
      thumbnails.forEach((thumb) => {
        thumb.addEventListener("click", () => {
          let getOriginalSrc = thumb.dataset.original;
          previewActive.setAttribute("src", getOriginalSrc);
          currentIndexRef.current = thumbnails.indexOf(thumb);
          removeClass(thumbnails, "active");
          thumb.classList.add("active");
        });
      });
    }
    showThumbsAsActive(thumbImagesRef.current, activeImageRef.current);

    function showAsActive() {
      activeImageRef.current.src =
        thumbImagesRef.current[currentIndexRef.current].dataset.original;
      removeClass(thumbImagesRef.current, "active");
      thumbImagesRef.current[currentIndexRef.current].classList.add("active");
      imageNumber();
    }
    function nextImage() {
      currentIndexRef.current++;
      if (currentIndexRef.current >= thumbImagesRef.current.length) {
        currentIndexRef.current = 0;
      }
      showAsActive();
    }
    function prevImage() {
      currentIndexRef.current--;
      if (currentIndexRef.current < 0) {
        currentIndexRef.current = thumbImagesRef.current.length - 1;
      }
      showAsActive(activeImageRef.current);
    }

    function imageNumber() {
      let currentImage = document.querySelector(
        ".preview-image-wrapper .count .current"
      );
      let totalImage = document.querySelector(
        ".preview-image-wrapper .count .total"
      );

      currentImage.textContent = currentIndexRef.current + 1;
      totalImage.textContent = thumbImagesRef.current.length;
    }
    imageNumber();

    function cloneSlider() {
      lightBoxContentRef.current.innerHTML = "";
      let elementToClone = document.querySelector(".product-images-wrapper");
      let clonedElement = elementToClone.cloneNode(true);
      let previewImageWrapper = clonedElement.querySelector(
        ".preview-image-wrapper"
      );
      let arrowsWrapper = clonedElement.querySelector(".arrows");
      let thumbsWrapper = clonedElement.querySelector(".thumbs-wrapper");

      arrowsWrapper.classList.remove("hide-for-desktop");
      thumbsWrapper.classList.remove("hide-for-mobile");
      // Add Close Button
      previewImageWrapper.innerHTML += `
        <div className="close-lightbox">
          <svg width="14" height="15" xmlns="http://www.w3.org/2000/svg">
            <title>close</title>
            <path
              d="m11.596.782 2.122 2.122L9.12 7.499l4.597 4.597-2.122 2.122L7 9.62l-4.595 4.597-2.122-2.122L4.878 7.5.282 2.904 2.404.782l4.595 4.596L11.596.782Z"
              fill="#FFF"
              fill-rule="evenodd"
            />
          </svg>
        </div>
      `;
      let closeBtn = previewImageWrapper.querySelector(".close-lightbox");
      lightBoxContentRef.current.appendChild(clonedElement);
      closeBtn?.addEventListener("click", closeLightBox);
      thumbImagesRef.current = Array.from(
        document.querySelectorAll(".lightbox-content .thumb-image")
      );
      nextBtnRef.current = document.querySelector(
        ".lightbox-content .arrows .next"
      );
      prevBtnRef.current = document.querySelector(
        ".lightbox-content .arrows .prev"
      );
      activeImageRef.current = document.querySelector(
        ".lightbox-content .preview-image"
      );
      showThumbsAsActive(thumbImagesRef.current, activeImageRef.current);
      nextBtnRef.current.addEventListener("click", () => {
        nextImage(activeImageRef.current);
      });
      prevBtnRef.current.addEventListener("click", () => {
        prevImage(activeImageRef.current);
      });
    }

    function removeClass(array, className) {
      array.forEach((element) => {
        element.classList.remove(className);
      });
    }

    function openOverlay() {
      overlayRef.current.classList.add("open");
    }

    function closeOverlay() {
      overlayRef.current.classList.remove("open");
    }
    overlayRef.current.addEventListener("click", (e) => {
      if (e.currentTarget === e.target) {
        closeOverlay();
      }
    });

    activeImageRef.current.addEventListener("click", () => {
      if (window.innerWidth >= 640) {
        openLightBox();
        cloneSlider();
      }
    });

    function openLightBox() {
      lightBoxWrapperRef.current.classList.add("open");
    }

    // Close Light Box Function
    function closeLightBox() {
      lightBoxWrapperRef.current.classList.remove("open");
    }

    // close Light Box When Click On the Overlay
    lightBoxWrapperRef.current.addEventListener("click", (e) => {
      if (e.currentTarget === e.target) closeLightBox();
    });
  }, []);

  return (
    <div>
      <Naavbar2/>
      <div className="p-4 flex my-0 mx-auto max-w-[1200px]">
        <main className="main">
          <section className="product-wrapper">
            <div className="container">
              <div className="product-images-wrapper">
                <div className="preview-image-wrapper">
                  <img
                    src="https://imgs.search.brave.com/6QnOioriOMsJ3G1lHrYO-Zl66AbylvdtJ7YfT_GNHEw/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTQx/MTc0OTEyNC9waG90/by9zdHlsaXNoLWJs/dWUtaGVhZHBob25l/cy5qcGc_cz02MTJ4/NjEyJnc9MCZrPTIw/JmM9Y0tZWjZRMk9j/QmVJWFdOT1g1MjFf/bFB1SUtfZ0gtcldP/LWxfb1hKbkxhTT0"
                    className="preview-image"
                    alt="Product Image"
                    width="900px"
                  />
                  <div className="arrows hide-for-desktop">
                    <div className="next">
                      <ArrowForwardIosIcon />
                    </div>
                    <div className="prev">
                      <ArrowBackIosNewIcon />
                    </div>
                  </div>
                  <div className="count">
                    <p>
                      <span className="current"></span> of
                      <span className="total"></span>
                    </p>
                  </div>
                </div>

                <div className="thumbs-wrapper hide-for-mobile">
                  <div className="thumb-image active">
                    <img
                      src="https://imgs.search.brave.com/6QnOioriOMsJ3G1lHrYO-Zl66AbylvdtJ7YfT_GNHEw/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTQx/MTc0OTEyNC9waG90/by9zdHlsaXNoLWJs/dWUtaGVhZHBob25l/cy5qcGc_cz02MTJ4/NjEyJnc9MCZrPTIw/JmM9Y0tZWjZRMk9j/QmVJWFdOT1g1MjFf/bFB1SUtfZ0gtcldP/LWxfb1hKbkxhTT0"
                      alt="Product Thumb Image"
                    />
                  </div>
                  <div className="thumb-image">
                    <img
                      src="https://imgs.search.brave.com/ka4PSFXZmYZWh4iKX5C1ymZDc4kiMaeCwfAe44aoXao/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZS5zaHV0dGVyc3Rv/Y2suY29tL2ltYWdl/LXBob3RvL2hpZ2hx/dWFsaXR5LWhlYWRw/aG9uZXMtb24td2hp/dGUtYmFja2dyb3Vu/ZC0yNjBudy0xNTc0/NjExOTkwLmpwZw"
                      alt="Product Thumb Image"
                    />
                  </div>
                  <div className="thumb-image">
                    <img
                      src="https://imgs.search.brave.com/W4o9VEdljaTDqztE40BJ2Q9v53XemQe4vle9tNceIN4/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvOTA5/MjM4Mjg2L3Bob3Rv/L3JlZC13aXJlbGVz/cy1oZWFkcGhvbmVz/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1mY3lTakhoXzBt/OFR5ZFM1eEVsSzR6/VWRycGFEdXZ6NGx1/Sm9ZNlNaT1RjPQ"
                      alt="Product Thumb Image"
                    />
                  </div>
                  <div className="thumb-image">
                    <img
                      src="https://imgs.search.brave.com/rru0Yb902yWiW6MVaUHBQ-a72e7iAPT70aXdD8xKDCI/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTQx/MjI0MDc3MS9waG90/by9oZWFkcGhvbmVz/LW9uLXdoaXRlLWJh/Y2tncm91bmQud2Vi/cD9iPTEmcz0xNzA2/NjdhJnc9MCZrPTIw/JmM9aW1yaThNTy1v/b1lXQTlZd1V0UDB4/TV9YcFY4czNUTU9q/WUV2ZEVKSjZ0bz0"
                      alt="Product Thumb Image"
                    />
                  </div>
                </div>
              </div>
              <div className="product-details-wrapper">
                <p className="product-category">category</p>
                <h1 className="product-title">Title</h1>
                <p className="product-brand">brand name</p>
                <p className="product-description">
                  about | Lorem ipsum dolor sit amet, consectetur adipiscing
                  elit. Donec eleifend tellus eu dolor condimentum, eget
                  dignissim felis congue. Mauris nec..
                </p>

                <div className="product-price">
                  <div className="current-price-wrapper">
                    <h2 className="current-price">$curr_price</h2>
                    <span className="discount">discount%</span>
                  </div>
                  <div className="previous-price-wrapper">
                    <span className="previous-price">$cut_price</span>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </main>
        <div className="lightbox-wrapper">
          <div className="lightbox-content"></div>
        </div>
        <div className="overlay"></div>
      </div>
    </div>
  );
};

export default ProductPage;
