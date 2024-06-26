import createMiddleware from "next-intl/middleware";
import { supportedLanguages } from "./translations";

export default createMiddleware({
  locales: supportedLanguages,
  defaultLocale: "en",
  localePrefix: "never",
});

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico|healthz).*)"],
};
