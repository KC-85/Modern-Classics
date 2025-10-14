// Read Django's csrftoken cookie
export function getCSRFToken(name = "csrftoken") {
  const m = document.cookie.match(new RegExp(`(?:^|; )${name}=([^;]*)`));
  return m ? decodeURIComponent(m[1]) : "";
}
