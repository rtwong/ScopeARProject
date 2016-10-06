using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class GameManager : MonoBehaviour {


    public static GameManager instance = null;

    public int count;
    private Text countText;


    void Awake()
    {
        //Check if instance already exists
        if (instance == null)

            //if not, set instance to this
            instance = this;

        //If instance already exists and it's not this:
        else if (instance != this)

            //Then destroy this. This enforces our singleton pattern, meaning there can only ever be one instance of a GameManager.
            Destroy(gameObject);

        //Sets this to not be destroyed when reloading scene
        DontDestroyOnLoad(gameObject);

    }



    // Use this for initialization
    void Start () {
        count = 0;
        countText = GameObject.Find("Canvas/Score").GetComponent<UnityEngine.UI.Text>();
        setCountText();

    }

    // Update is called once per frame
    void Update () {
        setCountText();
	}

    void setCountText()
    {
        countText.text = "Count: " + count.ToString();

    }
}
