(import functools
  [partial :as pt]
)

(import py_data
 [exec :as data]
)


(defn body [data]
  (let
    [
     table (cut data 1)
    ]
    ""
  )
)

(defn header-line [data]
 (let
   [
    header (get data 0)
   ]
 )
)

(defn header [data]
 "Convert py list to markdown table"
  (let
    [
     header (get data 0)
    ]
    (+ "| " ((. " | " join) header) " |")
  )
)

(defn exec [data]
 (+
   (header data)
   (header-line data)
   (body data)
 )
)

(defn main []
 (print (exec (data)))
)

(if (= __name__ "__main__")
 (main)
)
