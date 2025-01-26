(function makeNewSiteTitle() {
  const VALID_FILE_NAMES = [
    "prototype",
    "test",
    "sample",
    "mockup",
    "demo",
    "final",
    "draft",
  ];

  const VALID_FILE_TYPES = [
    "cpp",
    "css",
    "dxf",
    "html",
    "json",
    "js",
    "pde",
    "psd",
    "py",
    "scss",
    "sketch",
    "sldprt",
    "sh",
    "dng",
    "tsx",
    "nef",
    "jpeg",
    "tiff",
  ];
  const RANDOM_FILE_TYPE =
    VALID_FILE_TYPES[Math.floor(Math.random() * VALID_FILE_TYPES.length)];
  const RANDOM_FILE_NAME =
    VALID_FILE_NAMES[Math.floor(Math.random() * VALID_FILE_NAMES.length)];
  const title = document.getElementById("site-title");
  title.innerHTML = `tb_${RANDOM_FILE_NAME}.${RANDOM_FILE_TYPE}`;
})();

(function () {
  const links = document
    .getElementById("writing-nav")
    .getElementsByTagName("a");
  const currentUrl = location.href;
  console.log(links);
  for (const link of links) {
    if (link.href === currentUrl) {
      console.log("adding active");
      link.classList.add("active");
    }
  }
})();
