export default function customPrecision (value, x) {
    if (value && typeof value === "number") {
      return value.toFixed(x);
    }
  }