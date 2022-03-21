(import functools
  [partial :as pt]
)

(import py_data
 [exec :as data]
)

(defn exec [data]
 "Convert py list to markdown table"
  (let
    [
     header (get data 0)
     value (cut data 1)
    ]
    [
     (+
       [""]
       (list
        (map
         (fn [h] (str h))
         header
        )
       )
       [""]
     )
    ]
  )
)

(defn main []
  (for [row (exec (data))]
    (print #* row :sep " | " :end "\n")
  )
)

(if (= __name__ "__main__")
 (main)
)