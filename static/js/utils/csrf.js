/* jshint esversion: 11, jquery: true */
/* global global, describe, beforeEach, afterEach, jest, test, require, expect, bootstrap */

// Read Django's csrftoken cookie
export function getCSRFToken(name = "csrftoken") {
  const m = document.cookie.match(new RegExp(`(?:^|; )${name}=([^;]*)`));
  return m ? decodeURIComponent(m[1]) : "";
}
