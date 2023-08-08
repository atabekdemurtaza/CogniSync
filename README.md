# CogniSync API

Welcome to the API documentation for CognySync! This document outlines the available API routes for managing products.

## Base URL

The base URL for the API is `https://cognisync.com`.

## Available Routes

### List Products

- **Route:** `/api/products/`
- **Method:** GET
- **Description:** Get a list of all products.

### Create Product

- **Route:** `/api/products/create/`
- **Method:** POST
- **Description:** Create a new product.

### Upload Product Image

- **Route:** `/api/products/upload/`
- **Method:** POST
- **Description:** Upload an image for a product.

### List Product Reviews

- **Route:** `/api/products/<id>/reviews/`
- **Method:** GET
- **Description:** Get reviews for a specific product.

### List Top Products

- **Route:** `/api/products/top/`
- **Method:** GET
- **Description:** Get a list of top-rated products.

### Retrieve Product Details

- **Route:** `/api/products/<id>/`
- **Method:** GET
- **Description:** Get details for a specific product.

### Delete Product

- **Route:** `/api/products/delete/<id>/`
- **Method:** DELETE
- **Description:** Delete a specific product.

### Update Product

- **Route:** `/api/products/update/<id>/`
- **Method:** PUT
- **Description:** Update details for a specific product.

## Response Formats

- All responses are in JSON format.

## Authentication

- Authentication might be required for certain routes. Please refer to the route descriptions for details.

## Error Handling

- The API returns appropriate status codes and error messages in case of errors.

## Example Usage

```bash
curl -X GET https://cognisync.com/api/products/
