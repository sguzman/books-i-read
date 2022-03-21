(import py_data
 [exec :as data]
)

(import filter_read
 [exec :as readme]
)


(import filter_bad
 [exec :as bad]
)

(import __sort_by_date
 [exec :as dsort]
)

(import slim
 [exec :as slim]
)

(defn exec [data]
 "Return read books"
  (dsort (slim (readme (bad data))))
)

(defn main []
  (let [d (exec (data))]
    (for [row d]
      (print row)
    )
  )
)

(if (= __name__ "__main__")
 (main)
)
