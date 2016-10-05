Rails.application.routes.draw do
  resources :todo_items do
    member do
      patch :complete
    end
  end
  
  root "todo_items#index"
end
