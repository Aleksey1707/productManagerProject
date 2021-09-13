SELECT setval('product_category_id_seq',
              (SELECT product_category.id
               from product_category
               order by product_category.id desc
               limit 1),
              true);

SELECT setval('product_product_id_seq',
              (SELECT product_product.id
               from product_product
               order by product_product.id desc
               limit 1),
              true);


SELECT setval('product_shop_id_seq',
              (SELECT product_shop.id
               from product_shop
               order by product_shop.id desc
               limit 1),
              true);


SELECT setval('product_productstate_id_seq',
              (SELECT product_productstate.id
               from product_productstate
               order by product_productstate.id desc
               limit 1),
              true);
